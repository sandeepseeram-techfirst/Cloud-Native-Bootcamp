def main():
  random_bag = create_random_bag()
  display_bag()


def create_random_bag():
   marble1 = create_random_marble()
   marble2 = create_random_marble()
   marble3 = create_random_marble()
   return [marble1, marble2, marble3]
