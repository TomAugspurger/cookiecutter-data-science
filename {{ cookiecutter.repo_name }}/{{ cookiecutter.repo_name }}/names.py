"""
Basic project layout. Items in the project should refer items
in `ns`, not raw strings.

We prefer pathlib.Path objects where possible.
"""
from argparse import Namespace
from pathlib import Path

root = Path(__file__).parent.parent

ns = Namespace(
    data=Namespace(
        root=root / 'data',
        external=root / 'data/external',
        raw=root / 'data/raw',
        processed=root / 'data/processed',
    ),
    models=Namespace(
        root=root / 'models'
    ),
    notebooks=Namespace(
        root=root / 'notebooks',
    ),
    reports=Namespace(
        root=root / 'reports',
    ),
)

__all__ = ['ns']
