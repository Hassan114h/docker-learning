#Build stage
FROM python:3.8-slim AS build

WORKDIR /install
RUN pip install --no-cache-dir --prefix=/install flask pymysql

# Production stage
FROM python:3.8-slim AS final

WORKDIR /app
COPY --from=build /install /usr/local
COPY app.py .

EXPOSE 5000
CMD ["python", "app.py"]
