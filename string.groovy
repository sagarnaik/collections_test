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
