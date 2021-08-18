# cookiecutter-forge-lambda
This is a Cookiecutter template used for creating AWS Lambdas that can be built, deployed, and invoked by Forge.

REQUIRES:
* cookiecutter (https://github.com/audreyr/cookiecutter)

You can create a new Lambder project with cookiecutter:

    cookiecutter https://github.com/Lab183/cookiecutter-forge-lambda

But the best way is to just use [Forge](https://github.com/Lab183/ForgeApp):

    forge function create --name foo --bucket mybucket

See the [Forge README](https://github.com/Lab183/ForgeApp/blob/master/README.md) for more details.