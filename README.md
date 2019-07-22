# Rescale File Upload Testing

Installation and Execution
--------------------------

Run all required containers

```
$ docker-compose up -d
```

To run UI Tests

- Install VNC viewer: https://www.realvnc.com/en/connect/download/viewer/
- Start VNC viewer at localhost:5900 (password: secret)

```
$ docker exec test_runner pytest test/test_ui
```

To run API Tests

```
$ docker exec test_runner pytest test/test_api
```

To run API and UI Tests

```
$ docker exec test_runner pytest test
```

After completion

```
$ docker-compose down
```
