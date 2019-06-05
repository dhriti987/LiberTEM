import numpy as np

import libertem.udf.logsum as logsum

from utils import MemoryDataSet, _mk_random


def test_logsum(lt_ctx):
    data = _mk_random((16, 8, 32, 64))

    dataset = MemoryDataSet(data=data, tileshape=(8, 32, 64),
                            num_partitions=2, sig_dims=2)

    logsum_result = logsum.run_logsum(ctx=lt_ctx, dataset=dataset)

    minima = np.min(data, axis=(2, 3))
    naive_result = np.log(data - minima[..., np.newaxis, np.newaxis] + 1).sum(axis=(0, 1))

    assert np.allclose(logsum_result['logsum'].data, naive_result)
