# flake8: noqa
import os

import os.path as osp
from basicsr.train import train_pipeline

import realesrgan.archs
import realesrgan.data
import realesrgan.models


def get_last_weight():
    files_path = "experiments/train_RealESRNetx4plus_1000k_B12G4/models"
    pth_files = os.listdir(files_path)
    pth_files.sort(key=lambda x: int(x.split("_")[-1].split(".")[0]))
    higher_file = pth_files[-1]

    higher_file_path = files_path + "/" + higher_file
    return higher_file_path


def update_settings_file():
    file_path = "options/train_realesrnet_x4plus.yml"

    last_weight_path = get_last_weight()
    with open(file_path, "r") as f:
        lines = f.readlines()

    lines[91] = f"  pretrain_network_g: {last_weight_path}\n"
    print(lines)

    with open(file_path, "w") as f:
        f.writelines(lines)
    print(f"Line 92 in {file_path} has been updated with {last_weight_path}.")


if __name__ == "__main__":
    root_path = osp.abspath(osp.join(__file__, osp.pardir, osp.pardir))
    update_settings_file()
    train_pipeline(root_path)
