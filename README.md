## Quick Start

```bash
# Run in Docker
docker-compose up
# use -d flag to run in background
# use --build to force build (and clear mongo)

# Tear down
docker-compose down

# To be able to edit files, add volume to compose file
volumes: ['./:/usr/src/app']

# To re-build
docker-compose build
```
