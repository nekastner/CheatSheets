#include <cmocka.h>

#include <calculator.h>

static void test_sensor_processing(void **state)
{
    (void) state;

    const int result = add(1, 2);

    assert_int_equal(result, 3);
}

int main(void)
{
    const struct CMUnitTest tests[] = {
        cmocka_unit_test(test_sensor_processing),
    };

    return cmocka_run_group_tests(tests, NULL, NULL);
}