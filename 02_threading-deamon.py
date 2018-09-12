import threading


def print_something(something):
    print(something)

t = threading.Thread(target=print_something, args=('hello',))
# thread 를 daemon 으로 설정 했으므로 더이상 join 함수를 사용할 필요가 없다.
# daemon 으로 설정하면 메인 스레드가 종료하면 worker 스레드도 함께 종료 된다.
t.daemon = True
t.start()
print('thread started')
