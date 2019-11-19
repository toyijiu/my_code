//C++对定义于不同编译单元内的non-local static对象的初始化相对次序无明确定义,这样就容易出问题，一个文件调用另一个的non-static-object，就必须保证被调用的先定义才行
//解决方法是将每个non-local-static对象搬到static函数中，把non-static编程local-static，C++保证函数内的local static对象会在该函数被调用期间首次遇上该对象之定义式时
//被初始化，而且如果你不调用该函数，也就不会引发函数里的local-static对象的构造析构成本
//伪码
class FileSystem{...};

FileSystem& tfs()
{
    static FileSystem fs;
    return fs;
}

class Directory{...};
Directory::Directory(params)
{
    ...
    std::size_t disks = tfs().numDisks();
    ...
}

Directory& tempDir()
{
    static Directory td;
    return td;
}

