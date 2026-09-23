#include <cuda_runtime.h>
#include <math.h>
#include <float.h>

__device__ float atomicMaxFloat(float* address, float val)
{
    //chua hieu
    int* address_as_int = (int*)address;
    int old = *address_as_int;
    int assumed;

    do {
        assumed = old;

        float old_float = __int_as_float(assumed);
        if (old_float >= val)
            break;
        old = atomicCAS(address_as_int, assumed, __float_as_int(val));

    } while (assumed != old);

    return __int_as_float(old);
}

__global__ void softmax_max_kernel(const float* input, float* output, int N
)
{
    int i = blockDim.x * blockIdx.x + threadIdx.x;

    if (i < N)
    {
        atomicMaxFloat(output, input[i]);
    }
}

__global__ void softmax_sum_kernel(const float* input, float* output, int N, const float* max)
{
    int i = blockDim.x * blockIdx.x + threadIdx.x;

    if (i < N)
    {
        atomicAdd(output, expf(input[i] - *max));
    }
}

__global__ void softmax_kernel(const float* input, float* output, int N, const float* sum, const float* max)
{
    int i = blockDim.x * blockIdx.x + threadIdx.x;

    if (i < N)
    {
        output[i] = expf(input[i] - *max) / (*sum);
    }
}

extern "C" void solve(const float* input, float* output, int N)
{
    int threads = 256;
    int blocks = (N + threads - 1) / threads;

    float* max;
    float* sum;

    cudaMalloc(&max, sizeof(float));
    cudaMalloc(&sum, sizeof(float));
    
    //chua hieu
    float h_max = -FLT_MAX;
    cudaMemcpy(max, &h_max, sizeof(float), cudaMemcpyHostToDevice);
    cudaMemset(sum, 0, sizeof(float));

    softmax_max_kernel<<<blocks, threads>>>(input, max, N);
    softmax_sum_kernel<<<blocks, threads>>>(input, sum, N, max);
    softmax_kernel<<<blocks, threads>>>(input, output, N, sum, max);

    cudaDeviceSynchronize();

    cudaFree(max);
    cudaFree(sum);
}