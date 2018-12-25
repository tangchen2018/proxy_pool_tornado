# class DateUtilsBase(object):
#
#	 @staticmethod
#	 def get_today_start():
#		 now = arrow.utcnow().to("local")
#		 return now.floor("day")
#
#	 @staticmethod
#	 def get_today_end():
#		 now = arrow.utcnow().to("local")
#		 return now.ceil("day")
#
#	 @staticmethod
#	 def get_today_start_end():
#		 return DateUtilsBase.get_today_start(), DateUtilsBase.get_today_end()
#
#	 @staticmethod
#	 def get_week_start():
#		 now = arrow.utcnow().to("local")
#		 return now.floor("week")
#
#	 @staticmethod
#	 def get_week_end():
#		 now = arrow.utcnow().to("local")
#		 return now.ceil("week")
#
#	 @staticmethod
#	 def get_week_start_end():
#		 return DateUtilsBase.get_week_start(), DateUtilsBase.get_week_end()
#
#	 @staticmethod
#	 def get_month_start():
#		 now = arrow.utcnow().to("local")
#		 return now.floor("month")
#
#	 @staticmethod
#	 def get_month_end():
#		 now = arrow.utcnow().to("local")
#		 return now.ceil("month")
#
#	 @staticmethod
#	 def get_month_start_end():
#		 return DateUtilsBase.get_month_start(), DateUtilsBase.get_month_end()
#
#	 @staticmethod
#	 def get_quarter_start():
#		 now = arrow.utcnow().to("local")
#		 return now.floor("quarter")
#
#	 @staticmethod
#	 def get_quarter_end():
#		 now = arrow.utcnow().to("local")
#		 return now.ceil("quarter")
#
#	 @staticmethod
#	 def get_quarter_start_end():
#		 return DateUtilsBase.get_quarter_start(), DateUtilsBase.get_quarter_end()
#
#	 @staticmethod
#	 def get_year_start():
#		 now = arrow.utcnow().to("local")
#		 return now.floor("year")
#
#	 @staticmethod
#	 def get_year_end():
#		 now = arrow.utcnow().to("local")
#		 return now.ceil("year")
#
#	 @staticmethod
#	 def get_year_start_end():
#		 return DateUtilsBase.get_year_start(), DateUtilsBase.get_year_end()


class UserTimeBase(object):

    def __init__(self, timezone='local', arrow=None):

        self.arrow = arrow
        if not self.arrow:
            import arrow
            self.arrow = arrow
        #时区
        self.timezone = timezone

    # 获取当前时间的arrow结构
    @property
    def today(self):
        return self.arrow.now(self.timezone)

    # 当前时间戳
    @property
    def timestamp(self):
        return self.today.timestamp

    # 获取当前时间,自定义format
    def get_today_format(self, format_v="YYYY-MM-DD HH:mm:ss"):
        return self.today.format(format_v)

    # 时间戳转arrow
    def timestamp_to_arrow(self, timestamp=None):
        return self.arrow.get(timestamp).to(
            self.timezone) if timestamp else timestamp

    # arrow转时间戳
    def arrow_to_timestamp(self, arrow_v=None):
        return arrow_v.timestamp if arrow_v else arrow_v

    #arrow转字符串
    def arrow_to_string(self, arrow_s=None, format_v="YYYY-MM-DD HH:mm:ss"):
        return arrow_s.format(format_v) if arrow_s else arrow_s

    #字符串转arrow
    def string_to_arrow(self, string_s=None, format_v="YYYY-MM-DD HH:mm:ss"):
        return self.arrow.get(
            string_s, format_v, tzinfo=self.timezone) if string_s else string_s

    #时间戳转字符串
    def timestamp_to_string(self, timestamp, format_v="YYYY-MM-DD HH:mm:ss"):
        return self.arrow_to_string(
            self.timestamp_to_arrow(timestamp), format_v)

    #字符串转时间戳
    def string_to_timestamp(self, string_s=None,
                            format_v="YYYY-MM-DD HH:mm:ss"):
        return self.string_to_arrow(
            string_s, format_v).timestamp if string_s else string_s

    #时间日期加减
    def replace(self, arrow_v, **kwargs):
        """
			example :
				days = -1  减一天
				weeks = -1 减一周
				mounts = -1 减一个月
				quarters = -1 减一个季度
				years = -1 减一年
				hours = -1 减一小时
				minutes = -1 减一分钟
				seconds = -1 减一秒钟
		"""
        return arrow_v.replace(**kwargs)

    #判断周几
    def get_week_day(self, todays=None):
        """
			todays: "YYYY-MM-DD" 字符串
			周一:1 ... 周日:7
		"""
        format_v = "YYYY-MM-DD"
        day_arrow = self.today if not todays else self.string_to_arrow(
            todays, format_v)
        day_string = self.arrow_to_string(
            self.today, format_v) if not todays else self.arrow_to_string(
                self.string_to_arrow(todays, format_v), format_v)

        week1 = day_arrow.floor('week')
        if self.arrow_to_string(week1, format_v) == day_string:
            return 1
        elif self.arrow_to_string(week1.replace(days=1),
                                  format_v) == day_string:
            return 2
        elif self.arrow_to_string(week1.replace(days=2),
                                  format_v) == day_string:
            return 3
        elif self.arrow_to_string(week1.replace(days=3),
                                  format_v) == day_string:
            return 4
        elif self.arrow_to_string(week1.replace(days=4),
                                  format_v) == day_string:
            return 5
        elif self.arrow_to_string(week1.replace(days=5),
                                  format_v) == day_string:
            return 6
        elif self.arrow_to_string(week1.replace(days=6),
                                  format_v) == day_string:
            return 7
        else:
            return None


if __name__ == '__main__':

    times = UserTimeBase()
    print(times.get_week_day())
