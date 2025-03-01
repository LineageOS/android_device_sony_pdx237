#
# Copyright (C) 2018 The LineageOS Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# Inherit from sony sm8550-common
-include device/sony/sm8550-common/BoardConfigCommon.mk

DEVICE_PATH := device/sony/pdx237

# Display
TARGET_SCREEN_DENSITY := 420

# Kernel
TARGET_KERNEL_CONFIG += vendor/sony/pdx237.config

# Props
TARGET_VENDOR_PROP += $(DEVICE_PATH)/vendor.prop

# OTA
TARGET_OTA_ASSERT_DEVICE := pdx237,XQ-DE72

# inherit from the proprietary version
-include vendor/sony/pdx237/BoardConfigVendor.mk
