from __future__ import annotations

import ast
import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {'.git', '.github', '__pycache__'}


def files_with_suffix(suffix: str):
    for path in ROOT.rglob(f'*{suffix}'):
        if not any(part in SKIP_DIRS for part in path.parts):
            yield path


def check_python() -> list[str]:
    errors = []

    for path in files_with_suffix('.py'):
        try:
            source = path.read_text(encoding='utf-8')
            ast.parse(source, filename=str(path.relative_to(ROOT)))
        except (SyntaxError, UnicodeDecodeError) as error:
            errors.append(f'{path.relative_to(ROOT)}: {error}')

    return errors


LINK_RE = re.compile(r'(?<!!)\[[^\]]*\]\(([^)]+)\)')


def check_markdown_links() -> list[str]:
    errors = []

    for path in files_with_suffix('.md'):
        text = path.read_text(encoding='utf-8')

        for raw_target in LINK_RE.findall(text):
            target = raw_target.strip().split('#', 1)[0]

            if not target:
                continue

            if target.startswith(('http://', 'https://', 'mailto:')):
                continue

            target = unquote(target)
            resolved = (path.parent / target).resolve()

            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(
                    f'{path.relative_to(ROOT)}: ссылка выходит за пределы репозитория: {raw_target}'
                )
                continue

            if not resolved.exists():
                errors.append(
                    f'{path.relative_to(ROOT)}: не найдена ссылка {raw_target}'
                )

    return errors


def check_topic_pairs() -> list[str]:
    errors = []

    for section in ('ЕГЭ', 'ОГЭ'):
        base = ROOT / section

        if not base.exists():
            continue

        for topic in sorted(p for p in base.iterdir() if p.is_dir()):
            if not (topic / 'README.md').exists():
                errors.append(
                    f'{topic.relative_to(ROOT)}: нет README.md'
                )

    basics = ROOT / 'Python' / 'Основы'

    if basics.exists():
        for topic in sorted(p for p in basics.iterdir() if p.is_dir()):
            if not (topic / 'README.md').exists():
                errors.append(
                    f'{topic.relative_to(ROOT)}: нет README.md'
                )

            if not any(topic.glob('*.py')):
                errors.append(
                    f'{topic.relative_to(ROOT)}: нет Python-файла с примерами'
                )

    algorithms = ROOT / 'Алгоритмы'

    if algorithms.exists():
        for topic in sorted(p for p in algorithms.iterdir() if p.is_dir()):
            if not (topic / 'README.md').exists():
                errors.append(
                    f'{topic.relative_to(ROOT)}: нет README.md'
                )

            if not any(topic.glob('*.py')):
                errors.append(
                    f'{topic.relative_to(ROOT)}: нет Python-файла с примерами'
                )

    return errors


def main() -> int:
    checks = [
        ('Синтаксис Python', check_python()),
        ('Внутренние ссылки Markdown', check_markdown_links()),
        ('Структура учебных разделов', check_topic_pairs()),
    ]

    failed = False

    for name, errors in checks:
        if errors:
            failed = True
            print(f'\n[ОШИБКА] {name}')

            for error in errors:
                print(f'  - {error}')
        else:
            print(f'[OK] {name}')

    if failed:
        print('\nПроверка завершилась с ошибками.')
        return 1

    print('\nВсе автоматические проверки пройдены.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
