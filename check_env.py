"""
Python 环境测试脚本
验证所有必要的库是否正确安装
"""

def test_environment():
    """测试 Python 环境配置"""
    print("=" * 50)
    print("🔍 Python 环境检查")
    print("=" * 50)
    
    # 测试基础库
    libraries = {
        'sys': '系统库',
        'os': '系统库',
        'numpy': 'NumPy - 数值计算',
        'pandas': 'Pandas - 数据处理',
        'matplotlib': 'Matplotlib - 数据可视化',
        'seaborn': 'Seaborn - 统计可视化',
        'sklearn': 'Scikit-learn - 机器学习',
        'IPython': 'IPython - 增强 Python Shell',
        'jupyter': 'Jupyter - 笔记本环境'
    }
    
    success_count = 0
    failed_count = 0
    
    for lib, description in libraries.items():
        try:
            __import__(lib)
            print(f"✅ {lib:15} | {description}")
            success_count += 1
        except ImportError:
            print(f"❌ {lib:15} | {description} - 未安装")
            failed_count += 1
    
    print("=" * 50)
    print(f"✅ 成功: {success_count}/{len(libraries)}")
    if failed_count > 0:
        print(f"❌ 失败: {failed_count}/{len(libraries)}")
    print("=" * 50)
    
    # 显示 Python 版本信息
    import sys
    print(f"\n📌 Python 版本: {sys.version}")
    print(f"📌 Python 路径: {sys.executable}")
    
    if success_count == len(libraries):
        print("\n🎉 环境配置完美! 你可以开始学习 Python 了!")
    else:
        print("\n⚠️  部分库未安装，请运行:")
        print("   pip install -r requirements.txt")

if __name__ == '__main__':
    test_environment()
