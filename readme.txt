Input to the code:

    - 'input.txt' contains the test cases

    - each line contains a new test case

    - the items of cart should be seprated ','

    - Unknown items will be igored in the billing. (No exception will be raised.)


Instructions to run the code:

    - cd to the rackspace folder

    - build the image from the dockerfile
        * command: docker build -t farmer/market .

    - create the container and run it
        * command: docker run -ti --name farmer/market


Note: if the container name already exists, remove it.
    - command: docker rm market


Assumptions:
    - 'BOGO': coffee will only be free if its added in the cart.
    - 'APOM': the cost of each apple will be reduced to half after adding oatmeal.
