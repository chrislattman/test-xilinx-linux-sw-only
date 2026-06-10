# 2026-06-10T03:14:38.851543228
import vitis

client = vitis.create_client()
client.set_workspace(path="vitis")

status = client.set_preference(level = "WORKSPACE", device = "zynqMP", key = "sysroot", value = "/home/chris/test-xilinx-linux-sw-only/sw/embeddedlinux/images/linux/sdk/sysroots/cortexa72-cortexa53-amd-linux")

comp = client.get_component(name="linux_hello_world")
comp.build()

comp.set_app_config(key = "USER_LINK_LIBRARIES", values = ["libsystemd"])

comp.build()

comp.set_app_config(key = "USER_LINK_LIBRARIES", values = ["systemd"])

comp.build()

