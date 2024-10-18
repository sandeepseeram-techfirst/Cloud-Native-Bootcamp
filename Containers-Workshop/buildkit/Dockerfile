# syntax=docker/dockerfile:1.4
FROM node:20

# Cache npm dependencies
RUN --mount=type=cache,target=/app/node_modules \
    npm ci

# Copy source code separately to maximize caching
COPY . /app

# Final command
CMD ["node", "app.js"]