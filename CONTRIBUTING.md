# Contributing

When adding a new tool, it's helpful to only run a few tests, and to show shorter tracebacks. E.g. with

```
pytest check/tests/test_1_0_cellmlmanip.py --maxfail=3 --tb=short
```
