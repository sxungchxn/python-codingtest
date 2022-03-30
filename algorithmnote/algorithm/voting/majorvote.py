# nums 배열에서 major한 숫자를 찾는 Boyer-Moore 알고리즘


def majorityElement(self, nums):
    count = 0
    major = 0
    for num in nums:
        if count == 0:
            major = num
            count = 1
        else:
            if major == num:
                count += 1
            else:
                count -= 1
        return major
