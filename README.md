# soc-faker, a 2024 Clone

**This is a clone of the beloved original [soc-faker](https://github.com/swimlane/soc-faker) with some minor modifications.**
- The python-dev dependency was removed from the Dockerfile since it was causing errors and was not needed.
- The following methods were also causing failures, and thus were removed from bin/test.py:
  - print(sc.network.hostname)
  - print(sc.process.entity_id)
  - print(sc.process.parent)
  - print(sc.process.start)
