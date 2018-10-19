import os

def sample_env(a):
  print(a)
  return "ooo"


def sample():
  s = (lambda: sample_env)()
  print(os.getenv("HOME", s("aaa")))


if __name__ == '__main__':
    sample()
