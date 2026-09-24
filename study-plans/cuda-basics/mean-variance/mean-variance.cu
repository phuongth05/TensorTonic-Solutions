#include <cuda_runtime.h>

__global__ void sum_variance_kernel(const float* input, float* output, int N) {
    int i = blockDim.x * blockIdx.x + threadIdx.x;

    if (i < N)
    {
        atomicAdd(output, input[i]);
    }
}

__global__ void mean_variance_kernel(const float* input, float* mean_out, float* var_out, int N, const float* sum) {
    // Write code here
    int i = blockDim.x * blockIdx.x + threadIdx.x;

    if (i < N)
    {
        float mean = (*sum) / (float)N;
        float diff = input[i] - mean;

        atomicAdd(var_out, diff * diff);
    }
}

__global__ void mean_kernel(float* mean_out, int N) {
    *mean_out = *mean_out / (float)N;
}

__global__ void variance_kernel(float* var_out, int N) {
    *var_out = *var_out / (float)N;
}

extern "C" void solve(const float* input, float* mean_out, float* var_out, int N) {
    int threads = 256;
    int blocks = (N + threads - 1) / threads;
    cudaMemset(mean_out, 0, sizeof(float));
    cudaMemset(var_out, 0, sizeof(float));

    sum_variance_kernel<<<blocks, threads>>>(input, mean_out, N);
    mean_variance_kernel<<<blocks, threads>>>(input, mean_out, var_out, N, mean_out);
    mean_kernel<<<1, 1>>>(mean_out, N);
    variance_kernel<<<1, 1>>>(var_out, N);

    cudaDeviceSynchronize();
}
