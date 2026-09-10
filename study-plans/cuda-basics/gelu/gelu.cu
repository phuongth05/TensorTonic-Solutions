#include <cuda_runtime.h>
#include <math.h>

__global__ void gelu_kernel(const float* input, float* output, int N) {
    // Write code here

    int idx = blockIdx.x * blockDim.x + threadIdx.x;

    if (idx < N)
    {
        output[idx] = input[idx] * 0.5 * (1 + erf(input[idx] / std::sqrt(2.0f)));
    }
}

extern "C" void solve(const float* input, float* output, int N) {
    int threads = 256;
    dim3 blocks((N + 255) / 256);
    gelu_kernel<<<blocks, threads>>>(input, output, N);
    cudaDeviceSynchronize();
}
