"""
测试小波变换特征提取代码
"""

if __name__ == '__main__':
    input_file = '../resources/chapter4/demo/data/leleccum.mat'

    from scipy.io import loadmat

    mat = loadmat(input_file)
    signal = mat['leleccum'][0]

    import pywt

    coeffs = pywt.wavedec(signal, 'bior3.7', level=5)
