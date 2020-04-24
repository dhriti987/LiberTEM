import os


def get_use_cuda():
    ret = os.environ.get("LIBERTEM_USE_CUDA")
    if ret is not None:
        ret = int(ret)
    return ret


def set_use_cuda(cuda_device: int):
    os.environ["CUDA_VISIBLE_DEVICES"] = str(cuda_device)
    os.environ["LIBERTEM_USE_CUDA"] = str(cuda_device)
    os.environ.pop("LIBERTEM_USE_CPU", None)


def get_use_cpu():
    ret = os.environ.get("LIBERTEM_USE_CPU")
    if ret is not None:
        ret = int(ret)
    return ret


def set_use_cpu(cpu: int):
    os.environ.pop("LIBERTEM_USE_CUDA", None)
    os.environ["LIBERTEM_USE_CPU"] = str(cpu)


def get_backend():
    cuda = get_use_cuda()
    cpu = get_use_cpu()
    if cpu is not None and cuda is not None:
        raise RuntimeError(
            "Both LIBERTEM_USE_CPU and LIBERTEM_USE_CUDA set, expecting at most one"
        )
    if cuda is not None:
        return "cupy"
    else:
        return "numpy"
