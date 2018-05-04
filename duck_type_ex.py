    class Duck(object):
        def quack(self):
          print "Quack"


    class Mallard(object):
        def quack(self):
            print "Quack Quack"


    def shoot(bird):
        bird.quack()


    for target in [Duck(), Mallard()]:
        shoot(target)
