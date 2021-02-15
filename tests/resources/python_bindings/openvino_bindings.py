# -*- coding: utf-8 -*-
# Copyright (C) 2021 Intel Corporation
# SPDX-License-Identifier: Apache-2.0
import openvino.inference_engine as ie

print('OpenVINO version:', ie.get_version())
print('Available devices: ', ie.IECore().available_devices)
devices = ie.IECore().available_devices
for device in devices:
    versions = ie.IECore().get_versions(device)[device]
    print(f'    {device}: {versions.description}, {versions.major}.{versions.minor}.{versions.build_number}')
