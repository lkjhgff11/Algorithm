import re
def solution(emails):
    pattern = "[a-z\.]+@[a-z]+\.(com|net|org)"
    p = re.compile(pattern)

    cnt = 0
    for email in emails:
        m = p.match(email)
        if m:
            cnt += 1
    return cnt

emails = ["abc.def@x.com", "abc", "abc@defx", "abc@defx.xyz"]
print(solution(emails))
