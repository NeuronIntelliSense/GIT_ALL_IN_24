import math
import random


def create_one_sample():
    target = random.uniform(0, 10)
    predict = random.uniform(0, 10)
    return target, predict


def mae(num_samples):
    predicts = []
    targets = []
    sublosses = []
    total_loss = 0
    for _ in range(num_samples):
        target_i, predict_i = create_one_sample()
        targets.append(target_i)
        predicts.append(predict_i)

        subloss_i = abs(target_i - predict_i)
        sublosses.append(subloss_i)

        total_loss += subloss_i

    final_mae = total_loss / num_samples

    return predicts, targets, sublosses, final_mae


def mse(num_samples):
    predicts = []
    targets = []
    sublosses = []
    total_loss = 0
    for _ in range(num_samples):
        target_i, predict_i = create_one_sample()
        targets.append(target_i)
        predicts.append(predict_i)

        subloss_i = (target_i - predict_i) ** 2
        sublosses.append(subloss_i)

        total_loss += subloss_i

    final_mse = total_loss / num_samples
    return predicts, targets, sublosses, final_mse


def rmse(num_samples):
    predicts, targets, sublosses, final_mse = mse(num_samples=num_samples)
    final_rmse = math.sqrt(final_mse)

    return predicts, targets, sublosses, final_rmse


def display(num_samples, loss_function, predicts, targets, sublosses, final):
    for i in range(num_samples):
        print(f"loss name: {loss_function}, sample: {i}, pred: {
              predicts[i]}, target: {targets[i]}, loss: {sublosses[i]}")

    print(f"Final {loss_function}: {final}")


def exercise3():
    num_samples = input(
        "Input number of samples (integer number) which are generated: ")
    if not num_samples.isnumeric():
        print("Number of samples must be an integer number")
        return
    else:
        num_samples = int(num_samples)
        loss_function = input("Input loss name: ")
        if loss_function == 'MAE':
            predicts, targets, sublosses, final = mae(num_samples=num_samples)
        elif loss_function == 'MSE':
            predicts, targets, sublosses, final = mse(num_samples=num_samples)
        elif loss_function == 'RMSE':
            predicts, targets, sublosses, final = rmse(num_samples=num_samples)
        else:
            print("The loss function you input is not supported.")
            return

    display(num_samples=num_samples,
            loss_function=loss_function,
            predicts=predicts,
            targets=targets,
            sublosses=sublosses,
            final=final)
