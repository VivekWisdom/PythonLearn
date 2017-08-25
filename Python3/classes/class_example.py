#/usr/bin/python3

class Duck:
    def quack(self):
        print('Quack')
    def walk(self):
        print('Walk')

def main():
    donald = Duck()
    donald.quack()
    donald.walk()

if __name__ == '__main__':
    main()



