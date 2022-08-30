"""
@Name: assert_util.py
@Auth: wujiayong
@Date: 2022/8/10-18:52
@Desc: 
@Ver : 0.0.0
"""

from json import JSONDecodeError

import jsonpath

from util.logUtli import logger


class Assert:

    def reqAssert(self, validates, resonpse):
        """
        api 包含and相等断言
        :param validates: 断言列表
        :type resonpse: requests 的返回值
        """
        all_fail = 0
        all_count = 0
        all_success = 0
        for validate in validates:
            for key, value in validate.items():
                if key == "equals" and value:
                    fail, success, count = self.__equals(value, resonpse)
                    all_fail = all_fail + fail
                    all_count = all_count + count
                    all_success = all_success + success
                elif key == 'contains' and value:
                    fail, success, count = self.__contains(value, resonpse)
                    all_fail = all_fail + fail
                    all_count = all_count + count
                    all_success = all_success + success
        try:
            assert all_fail == 0 and all_count == all_success != 0
            logger.info("断言成功:全部断言通过")
            logger.info("用例执行:成功")
        except AttributeError as e:
            logger.warning("断言:成功{}个，失败{}个,总计{}个".format(all_success, all_fail, all_count))
            logger.debug("用例执行:失败")

    def __equals(self, value, resonpse):
        """
        相等断言
        :param value: 断言列表中的equals字典
        :param resonpse: requests 的返回值
        :return: fail（失败）, success（成功）, count（总数）
        """
        fail = 0
        count = 0
        success = 0
        for assert_key, assert_value in value.items():

            if assert_key == "status_code":  # 状态断言
                count = count + 1
                if str(assert_value) == str(resonpse.status_code):
                    success = success + 1
                    logger.info("断言成功:返回的状态码等于%s" % assert_value)
                else:
                    fail = fail + 1
                    logger.debug("断言失败:返回的状态码不等于%s" % assert_value)
            else:
                try:
                    return_json = resonpse.json()
                except JSONDecodeError as e:
                    logger.warning('异常:请求返回的结果不为JSON格式')
                    logger.warning("异常原因:{}".format(e))
                else:
                    count = count + 1
                    return_value = jsonpath.jsonpath(return_json, '$...%s' % assert_key)[0]
                    if str(assert_value) == str(return_value):
                        success = success + 1
                        logger.info("断言成功:{}等于{}".format(assert_key, assert_value))
                    elif assert_value != return_value:
                        fail = fail + 1
                        logger.debug("断言失败:{}不等于{}".format(assert_key, assert_value))
                    else:
                        fail = fail + 1
                        logger.debug("断言失败：返回的结果不存在{}".format(assert_key))

        return fail, success, count

    def __contains(self, value, resonpse):
        """
        包含断言
        :param value: 包含断言字典值
        :param resonpse: requests 的返回值
        :return: fail（失败）, success（成功）, count（总数）
        """
        fail = 0
        count = 1
        success = 0
        if value in str(resonpse.text):
            success = success + 1
            logger.info("断言成功:返回的结果中包含{}".format(value))
        else:
            fail = fail + 1
            logger.debug("断言失败:返回的结果中不包含{}".format(value))
        return fail, success, count

    def driverAssert(self, validates, driver):
        """
        ui包含断言
        :param validates:
        :param driver:
        :return:
        """
        for validate in validates:
            for key, value in validate.items():
                if key == 'contains' and value:
                    try:
                        assert value in str(driver.page_source)
                        logger.info("断言成功:返回的结果中包含{}".format(value))
                        logger.info("用例执行:成功")
                    except AttributeError:
                        logger.debug("断言失败:返回的结果中不包含{}".format(value))
                        logger.debug("用例执行:失败")




