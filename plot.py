import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def plot_throughput():

    x = np.array([2, 4, 8, 16, 32, 64])
    y = np.array([1582.04, 3004.51, 5805.14, 11273.57, 19496.10, 33080.03])

    plt.figure(figsize=(7, 4))
    plt.plot(x, y, color='blue', marker='o')
    plt.xticks(x)
    plt.yticks(y)
    plt.xlabel('Number of GPUs')
    plt.ylabel('Training Throughput (images/sec)')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('figures/training_throughput.pdf')
    plt.savefig('figures/training_throughput.png')
    plt.show()


def plot_training_time():
    x = np.array([2, 4, 8, 16, 32, 64])
    y = np.array([74211.11, 39536, 20904.01, 10969.42, 6652.91, 4071.31])

    plt.figure(figsize=(7, 4))
    plt.plot(x, y, color='blue', marker='o')
    plt.xticks(x)
    plt.yticks(y)
    plt.xlabel('Number of GPUs')
    plt.ylabel('Training Time (secs)')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('figures/training_time.pdf')
    plt.savefig('figures/training_time.png')
    plt.show()


def smooth(scalars, smooth_factor):
    """
    Smoothing by exponential moving average
    :param scalars:
    :param smooth_factor:
    :return: smoothed scalars
    """
    last = scalars[0]  # First value in the plot (first timestep)
    smoothed = []
    for point in scalars:
        smoothed_val = last * smooth_factor + (1 - smooth_factor) * point  # Calculate smoothed value
        smoothed.append(smoothed_val)                        # Save it
        last = smoothed_val                                  # Anchor the last smoothed value

    return np.array(smoothed)


def plot_one_curve(ax, csv_path, color, label):
    df = pd.read_csv(csv_path)
    x, y = df['Step'], df['Value']
    y = smooth(y, 0.6)
    ax.plot(x, y, color=color, label=label)

    return ax


def plot_top1_train():
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.set(xlabel='Epochs',
           ylabel='Top-1 Train Accuracy')
    ax.grid()

    plot_one_curve(ax, 'Top1_train/run-Feb09_14-20-42_hal14_resnet50_gpux2_b208_cpu20_optO2-tag-Top1_train.csv', 'orange', 'gpux2')
    plot_one_curve(ax, 'Top1_train/run-Feb09_14-22-11_hal13_resnet50_gpux4_b208_cpu20_optO2-tag-Top1_train.csv', 'red', 'gpux4')
    plot_one_curve(ax, 'Top1_train/run-Feb08_13-47-09_hal11_resnet50_gpux8_b208_cpu20_optO2-tag-Top1_train.csv', 'blue', 'gpux8')
    plot_one_curve(ax, 'Top1_train/run-Feb09_09-21-23_hal13_resnet50_gpux16_b208_cpu20_optO2-tag-Top1_train.csv', 'purple', 'gpux16')
    plot_one_curve(ax, 'Top1_train/run-Feb12_23-28-54_hal01_resnet50_gpux32_b208_cpu20_optO2-tag-Top1_train.csv', 'brown', 'gpux32')
    plot_one_curve(ax, 'Top1_train/run-Feb12_21-54-28_hal01_resnet50_gpux64_b208_cpu20_optO2-tag-Top1_train.csv', 'gray', 'gpux64')

    plt.legend(loc='lower right')
    plt.tight_layout()
    fig.savefig('figures/top1_train.pdf')
    fig.savefig('figures/top1_train.png')
    plt.show()


def plot_top1_val():
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.set(xlabel='Epochs',
           ylabel='Top-1 Validation Accuracy')
    ax.grid()

    plot_one_curve(ax, 'Top1_val/run-Feb09_14-20-42_hal14_resnet50_gpux2_b208_cpu20_optO2-tag-Top1_val.csv', 'orange', 'gpux2')
    plot_one_curve(ax, 'Top1_val/run-Feb09_14-22-11_hal13_resnet50_gpux4_b208_cpu20_optO2-tag-Top1_val.csv', 'red', 'gpux4')
    plot_one_curve(ax, 'Top1_val/run-Feb08_13-47-09_hal11_resnet50_gpux8_b208_cpu20_optO2-tag-Top1_val.csv', 'blue', 'gpux8')
    plot_one_curve(ax, 'Top1_val/run-Feb09_09-21-23_hal13_resnet50_gpux16_b208_cpu20_optO2-tag-Top1_val.csv', 'purple', 'gpux16')
    plot_one_curve(ax, 'Top1_val/run-Feb12_23-28-54_hal01_resnet50_gpux32_b208_cpu20_optO2-tag-Top1_val.csv', 'brown', 'gpux32')
    plot_one_curve(ax, 'Top1_val/run-Feb12_21-54-28_hal01_resnet50_gpux64_b208_cpu20_optO2-tag-Top1_val.csv', 'gray', 'gpux64')

    plt.legend(loc='lower right')
    plt.tight_layout()
    fig.savefig('figures/top1_val.pdf')
    fig.savefig('figures/top1_val.png')
    plt.show()


def plot_top5_train():
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.set(xlabel='Epochs',
           ylabel='Top-5 Train Accuracy')
    ax.grid()

    plot_one_curve(ax, 'Top5_train/run-Feb09_14-20-42_hal14_resnet50_gpux2_b208_cpu20_optO2-tag-Top5_train.csv', 'orange', 'gpux2')
    plot_one_curve(ax, 'Top5_train/run-Feb09_14-22-11_hal13_resnet50_gpux4_b208_cpu20_optO2-tag-Top5_train.csv', 'red', 'gpux4')
    plot_one_curve(ax, 'Top5_train/run-Feb08_13-47-09_hal11_resnet50_gpux8_b208_cpu20_optO2-tag-Top5_train.csv', 'blue', 'gpux8')
    plot_one_curve(ax, 'Top5_train/run-Feb09_09-21-23_hal13_resnet50_gpux16_b208_cpu20_optO2-tag-Top5_train.csv', 'purple', 'gpux16')
    plot_one_curve(ax, 'Top5_train/run-Feb12_23-28-54_hal01_resnet50_gpux32_b208_cpu20_optO2-tag-Top5_train.csv', 'brown', 'gpux32')
    plot_one_curve(ax, 'Top5_train/run-Feb12_21-54-28_hal01_resnet50_gpux64_b208_cpu20_optO2-tag-Top5_train.csv', 'gray', 'gpux64')

    plt.legend(loc='lower right')
    plt.tight_layout()
    fig.savefig('figures/top5_train.pdf')
    fig.savefig('figures/top5_train.png')
    plt.show()


def plot_top5_val():
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.set(xlabel='Epochs',
           ylabel='Top-5 Validation Accuracy')
    ax.grid()

    plot_one_curve(ax, 'Top5_val/run-Feb09_14-20-42_hal14_resnet50_gpux2_b208_cpu20_optO2-tag-Top5_val.csv', 'orange', 'gpux2')
    plot_one_curve(ax, 'Top5_val/run-Feb09_14-22-11_hal13_resnet50_gpux4_b208_cpu20_optO2-tag-Top5_val.csv', 'red', 'gpux4')
    plot_one_curve(ax, 'Top5_val/run-Feb08_13-47-09_hal11_resnet50_gpux8_b208_cpu20_optO2-tag-Top5_val.csv', 'blue', 'gpux8')
    plot_one_curve(ax, 'Top5_val/run-Feb09_09-21-23_hal13_resnet50_gpux16_b208_cpu20_optO2-tag-Top5_val.csv', 'purple', 'gpux16')
    plot_one_curve(ax, 'Top5_val/run-Feb12_23-28-54_hal01_resnet50_gpux32_b208_cpu20_optO2-tag-Top5_val.csv', 'brown', 'gpux32')
    plot_one_curve(ax, 'Top5_val/run-Feb12_21-54-28_hal01_resnet50_gpux64_b208_cpu20_optO2-tag-Top5_val.csv', 'gray', 'gpux64')

    plt.legend(loc='lower right')
    plt.tight_layout()
    fig.savefig('figures/top5_val.pdf')
    fig.savefig('figures/top5_val.png')
    plt.show()


def plot_IO():
    df = pd.read_csv('IO/bandwidth_gpux64.csv', sep=";")
    y = df['Read'] / 1.0e9
    print("Average BW: {}".format(np.sum(y[10:60]) / 50.0))
    x = np.arange(len(y))

    fig, ax1 = plt.subplots(figsize=(7, 4))
    color1 = 'tab:blue'
    ax1.set_xlabel('Minutes')
    ax1.set_ylabel('Bandwidth (GBs)', color=color1)
    ax1.plot(x, y, color=color1)
    ax1.tick_params(axis='y', labelcolor=color1)

    df = pd.read_csv('IO/iops_gpux64.csv', sep=";")
    z = df['Read'] / 1000.0
    print("Average IOPS: {}".format(np.sum(z[10:60]) / 50.0))
    ax2 = ax1.twinx()
    color2 = 'tab:orange'
    ax2.set_ylabel('K IOPS', color=color2)
    ax2.plot(x, z, color=color2)
    ax2.tick_params(axis='y', labelcolor=color2)

    plt.tight_layout()
    fig.savefig('figures/IO.pdf')
    fig.savefig('figures/IO.png')
    plt.show()


if __name__ == '__main__':
    plot_throughput()
    # plot_training_time()
    # plot_top1_train()
    # plot_top1_val()
    # plot_top5_train()
    # plot_top5_val()
    # plot_IO()
