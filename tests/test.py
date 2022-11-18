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
        encoding_test = pydraco.encode_point_cloud(point_cloud_object.points, point_cloud_object.rgba,
                                                   point_cloud_object.normal, rgba_len, normal_len,
                                                   quantization_bits, compression_level,
                                                   quantization_range, quant_origin, create_metadata)
        with open("output.drc", "wb") as test_file:
            test_file.write(bytes(encoding_test.buffer))

    with open("output.drc", "rb") as test_file:
        file_content = test_file.read()
        point_cloud_object = pydraco.decode_buffer_to_point_cloud(file_content, len(file_content))
        print("Points Number:", len(point_cloud_object.points))


decode_encode_file()
