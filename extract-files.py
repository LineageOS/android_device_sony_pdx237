#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'hardware/qcom-caf/sm8550',
    'vendor/qcom/opensource/commonsys-intf/display',
    'vendor/sony/sm8550-common',
]


blob_fixups: blob_fixups_user_type = {
    'vendor/lib64/libarcsoft_hdr_adapter.so': blob_fixup()
        .add_needed('liblog.so')
        .add_needed('libcutils.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'pdx237',
    'sony',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(
        module, 'sm8550-common', module.vendor
    )
    utils.run()
