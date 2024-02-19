#!/usr/bin/groovy
// contains functions to be imported and used by all QA jenkins jobs

// Returns only files that were changed
def get_test_files()
{
    def test_files = []
    def str = sh(script: "df -h", returnStdout: true)
    println str

    for (_test in str.split('\n'))
    {
        test_name = _test
        if (test_name.contains("dev"))
        {
            test_files << test_name
        }
    }
    for (int i = 0; i < 20; i++) {
        sh "echo Hello"
    }
    return test_files
}

def while_check()
{
    count = 1
    while(count<5) {
         println(count);
         count++;
    }
    for(int i in 1..5) {
         println(i);
    }
}

def if_check(count=3)
{
    if (count < 5) {
        println("less than 5");
    }
    else if (count > 5){
        println("greater than 5");
    }
}
return this
