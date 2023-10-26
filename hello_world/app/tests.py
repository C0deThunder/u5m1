from django.test import SimpleTestCase


class TestHelloView(SimpleTestCase):
    def test_hello_wyatt(self):
        response = self.client.get("/hello/wyatt/")
        self.assertContains(response, "Hello wyatt!")

    def test_hello_world(self):
        response = self.client.get("/hello/world/")
        self.assertContains(response, "Hello world!")

class TestAddView(SimpleTestCase):
    def test_add_1_to_4(self):
        response = self.client.get("/add/1/4/")
        self.assertContains(response, "5")

    def test_add_1_to_9(self):
        response = self.client.get("/add/1/9/")
        self.assertContains(response, "10")