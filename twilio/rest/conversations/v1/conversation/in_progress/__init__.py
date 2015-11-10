# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import deserialize
from twilio import values
from twilio.instance_resource import InstanceResource
from twilio.list_resource import ListResource
from twilio.page import Page
from twilio.rest.conversations.v1.conversation.participant import ParticipantList


class InProgressList(ListResource):

    def __init__(self, version):
        """
        Initialize the InProgressList
        
        :param Version version: Version that contains the resource
        
        :returns: InProgressList
        :rtype: InProgressList
        """
        super(InProgressList, self).__init__(version)
        
        # Path Solution
        self._solution = {}
        self._uri = '/Conversations/InProgress'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams InProgressInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)
        
        :returns: Generator that will yield up to limit results
        :rtype: generator
        """
        limits = self._version.read_limits(limit, page_size)
        
        page = self.page(
            page_size=limits['page_size'],
        )
        
        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def read(self, limit=None, page_size=None):
        """
        Reads InProgressInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. read() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, read() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)
        
        :returns: Generator that will yield up to limit results
        :rtype: generator
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of InProgressInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50
        
        :returns: Page of InProgressInstance
        :rtype: Page
        """
        params = values.of({
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })
        
        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )
        
        return InProgressPage(
            self._version,
            response,
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Conversations.V1.InProgressList>'


class InProgressPage(Page):

    def __init__(self, version, response):
        """
        Initialize the InProgressPage
        
        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        
        :returns: InProgressPage
        :rtype: InProgressPage
        """
        super(InProgressPage, self).__init__(version, response)
        
        # Path Solution
        self._solution = {}

    def get_instance(self, payload):
        """
        Build an instance of InProgressInstance
        
        :param dict payload: Payload response from the API
        
        :returns: InProgressInstance
        :rtype: InProgressInstance
        """
        return InProgressInstance(
            self._version,
            payload,
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Conversations.V1.InProgressPage>'


class InProgressInstance(InstanceResource):

    def __init__(self, version, payload):
        """
        Initialize the InProgressInstance
        
        :returns: InProgressInstance
        :rtype: InProgressInstance
        """
        super(InProgressInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'status': payload['status'],
            'duration': deserialize.integer(payload['duration']),
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'start_time': deserialize.iso8601_datetime(payload['start_time']),
            'end_time': deserialize.iso8601_datetime(payload['end_time']),
            'account_sid': payload['account_sid'],
            'url': payload['url'],
        }
        
        # Context
        self._context = None
        self._solution = {}

    @property
    def sid(self):
        """
        :returns: The sid
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def status(self):
        """
        :returns: The status
        :rtype: in_progress.status
        """
        return self._properties['status']

    @property
    def duration(self):
        """
        :returns: The duration
        :rtype: unicode
        """
        return self._properties['duration']

    @property
    def date_created(self):
        """
        :returns: The date_created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def start_time(self):
        """
        :returns: The start_time
        :rtype: datetime
        """
        return self._properties['start_time']

    @property
    def end_time(self):
        """
        :returns: The end_time
        :rtype: datetime
        """
        return self._properties['end_time']

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def participants(self):
        """
        Access the participants
        
        :returns: participants
        :rtype: participants
        """
        return self._proxy.participants

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Conversations.V1.InProgressInstance>'
