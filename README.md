# CMU-17625-gRPC
gRPC and Protocol Buffers

Protocol buffer generation:

Go to root directory of the project.
Run the following command:


```python3 -m grpc_tools.protoc -I./protos protos/* --python_out=./service --grpc_python_out=./service --pyi_out=./service```
