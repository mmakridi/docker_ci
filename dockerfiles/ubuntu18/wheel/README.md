Build with:

```sh
cd <docker_ci>/dockerfiles/ubuntu18/wheel
cp <wheel_file> ./
docker build --build-arg package_url=./<wheel_file> --tag <image_repo>:<image_tag> .
```

Run tests with:

```sh
cd <docker_ci>
python3 ./docker_openvino.py test --tags <image_repo>:<image_tag> --distribution custom-full -k wheel
```