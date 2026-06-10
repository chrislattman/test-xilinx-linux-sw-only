# 2026-03-27T01:03:32.513019126
import vitis

client = vitis.create_client()
client.set_workspace(path="vitis")

advanced_options = client.create_advanced_options_dict(dt_overlay="0")

platform = client.create_platform_component(name = "ultra96v2_platform",hw_design = "$COMPONENT_LOCATION/../../../fpga/ultra96v2_wrapper.xsa",os = "linux",cpu = "psu_cortexa53",domain_name = "linux_psu_cortexa53",advanced_options = advanced_options)

platform = client.get_component(name="ultra96v2_platform")
status = platform.build()

status = client.set_preference(level = "WORKSPACE", device = "zynqMP", key = "sysroot", value = "/home/chris/test-xilinx-linux-sw-only/sw/embeddedlinux/images/linux/sdk/sysroots/cortexa72-cortexa53-amd-linux")

comp = client.create_app_component(name="linux_hello_world",platform = "$COMPONENT_LOCATION/../ultra96v2_platform/export/ultra96v2_platform/ultra96v2_platform.xpfm",domain = "linux_psu_cortexa53",template = "linux_hello_world")

comp = client.get_component("linux_hello_world")

status = comp.set_sysroot(sysroot="/home/chris/test-xilinx-linux-sw-only/sw/embeddedlinux/images/linux/sdk/sysroots/cortexa72-cortexa53-amd-linux")

comp = client.get_component(name="linux_hello_world")
comp.build()

comp.build()

comp.build()

vitis.dispose()

