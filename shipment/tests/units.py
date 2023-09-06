from time import sleep
from unittest import mock

from django.conf import settings
from django.core.cache import cache
from django.test import TestCase

import requests

from ..utils import ForcastUtility


class TestForcastUtility(TestCase):
    def tearDown(self) -> None:
        cache.clear()

    @mock.patch.object(cache, "get", return_value=False)
    @mock.patch.object(cache, "set", return_value=None)
    @mock.patch("shipment.utils.ForcastUtility._get_coordinates")
    def test_forcast_api_call_fails(
        self, mocked_coordiante_func, mocked_cache_set, mocked_cache_get
    ):
        # Call forcast api with incorrect values. caching mechanism should try to get the value once.
        # it should fail to return a value. Then since the url call has failed cache setting mechanism should get bypassed.
        # a N/A value is returned.

        mocked_coordiante_func.return_value = {"lat": "123", "lon": "123"}
        result = ForcastUtility(country="France", zip_code="75001").forcast()
        mocked_cache_get.assert_called_once()
        mocked_cache_set.assert_not_called()
        self.assertEqual(result, "N/A")

    @mock.patch.object(requests, "get")
    @mock.patch("shipment.utils.ForcastUtility._get_coordinates")
    def test_forcast_api_call_success(self, mocked_coordiante_func, mocked_request):
        # call the api once. Getting the value is not possible at the first try. But the method is called once.
        # The external API is called and returns a value. resp.ok passes so cache setting mechanism is called once and cache is set.
        # The api call is returned and value exists in the cache if called by cache.get() method.
        def res():
            r = requests.Response()
            r.status_code = 200

            def json_func():
                return {"weather": [{"description": "fake forcast"}]}

            r.json = json_func

            @property
            def ok():
                return True

            return r

        mocked_request.return_value = res()
        mocked_coordiante_func.return_value = {"lat": "123", "lon": "123"}
        result = ForcastUtility(country="France", zip_code="75001").forcast()
        self.assertEqual(cache.get("123:123"), "fake forcast")
        self.assertEqual(result, "fake forcast")

    @mock.patch("shipment.utils.ForcastUtility._get_coordinates")
    @mock.patch.object(requests, "get")
    @mock.patch.object(ForcastUtility, "CACHE_TIMEOUT", new_callable=mock.PropertyMock)
    def test_cache_expires_success(
        self, mocked_forcastutility_timeout, mocked_request, mocked_coordiante_func
    ):
        # A cache value is set. The timeout is set to 5 seconds. The first api call is without the 5 second timeout boundary.
        # hence the api call is bypassed. But after sleeping for five seconds the second api call can't get the value by calling cache.get()
        # because the timeout has expired and cache values have been cleared.

        # clear the cache just to make sure, even though TearDown method already took care of that.
        cache.clear()

        # set timeout for class attribute and assert cache timeout is set to 5 seconds.
        mocked_forcastutility_timeout.return_value = 5
        self.assertEqual(ForcastUtility.CACHE_TIMEOUT, 5)

        def res():
            r = requests.Response()
            r.status_code = 200

            def json_func():
                return {"weather": [{"description": "fake forcast"}]}

            r.json = json_func

            @property
            def ok():
                return True

            return r

        mocked_request.return_value = res()
        mocked_coordiante_func.return_value = {"lat": "123", "lon": "123"}
        result = ForcastUtility(country="France", zip_code="75001").forcast()

        # cache is set and here we can get the cache.
        self.assertEqual(cache.get("123:123"), "fake forcast")
        self.assertEqual(result, "fake forcast")

        # wait for five seconds
        sleep(5)

        # cache should be empty now.
        self.assertEqual(cache.get("123:123", False), False)
