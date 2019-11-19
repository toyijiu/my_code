//析构函数绝对不要吐出异常，如果一个析构函数可能抛出异常，析构函数应该捕捉任何异常，然后吞下异常或者结束程序
//如果客户需要对某个操作函数运行期间抛出的异常做出反应，class应提供一个普通函数来执行该操作
//析构函数吐出异常就是危险

class DBConnection{
    public:
        static DBConnection create();

        void close();
};

class DBConn{
    public:
        void close(){
            db.close();
            closed = true;
        }

        ~DBConn(){
            if(!closed){
                try{
                    db.close();
                }
                catch(...){
                    ...
                }
            }
            
        }
    private:
        DBConnection db;
        bool closed;
};