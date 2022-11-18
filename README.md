# pydraco

A python wrapper for the Google Draco https://github.com/google/draco

## Prerequisites

**Tested Env**

* Ubuntu 18.04
* python 3.8.10
* CMake 3.22.4
* Ninja or Pip 10+


## Installation

Clone this repository, compile & install.

```bash
git clone --recursive https://github.com/JinghaoZhao/pydraco.git
cd pydraco
python setup.py build
python setup.py install
```

With the `setup.py` file included in this example, the `pip install` command will
invoke CMake and build the pybind11 module as specified in `CMakeLists.txt`.


## License

pydraco is provided under Apache License. By using, distributing, or contributing to this project, you agree to the
terms and conditions of this license.


## Sample Usage

```python
import pydraco

def decode_encode_file():
    with open("sample.drc", "rb") as drc_file:
        file_content = drc_file.read()
        point_cloud_object = pydraco.decode_buffer_to_point_cloud(file_content, len(file_content))
        print("Points Number:", len(point_cloud_object.points))
        rgba_len = 3
        normal_len = 0
        quantization_bits = 14
        compression_level = 1
        quantization_range = 1
        quant_origin = 0
        create_metadata = False
        encoding_test = pydraco.encode_point_cloud(point_cloud_object.points, point_cloud_object.rgba, point_cloud_object.normal,
                                                   rgba_len, normal_len,
                                                   quantization_bits, compression_level,
                                                   quantization_range, quant_origin, create_metadata)
        with open("output.drc", "wb") as test_file:
            test_file.write(bytes(encoding_test.buffer))

    with open("output.drc", "rb") as test_file:
        file_content = test_file.read()
        point_cloud_object = pydraco.decode_buffer_to_point_cloud(file_content, len(file_content))
        print("Points Number:", len(point_cloud_object.points))

decode_encode_file()
```

[`cibuildwheel`]:          https://cibuildwheel.readthedocs.io
[FAQ]: http://pybind11.rtfd.io/en/latest/faq.html#working-with-ancient-visual-studio-2009-builds-on-windows
[vs2015_runtime]: https://www.microsoft.com/en-us/download/details.aspx?id=48145
[scikit-build]: https://scikit-build.readthedocs.io/en/latest/
