# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import glossary_pb2 as app_dot_glossary__pb2

GRPC_GENERATED_VERSION = '1.68.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in app/glossary_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class GlossaryServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAllTerms = channel.unary_unary(
                '/dictionary.GlossaryService/GetAllTerms',
                request_serializer=app_dot_glossary__pb2.Empty.SerializeToString,
                response_deserializer=app_dot_glossary__pb2.TermsList.FromString,
                _registered_method=True)
        self.AddTerm = channel.unary_unary(
                '/dictionary.GlossaryService/AddTerm',
                request_serializer=app_dot_glossary__pb2.Term.SerializeToString,
                response_deserializer=app_dot_glossary__pb2.MessageResponse.FromString,
                _registered_method=True)
        self.GetTerm = channel.unary_unary(
                '/dictionary.GlossaryService/GetTerm',
                request_serializer=app_dot_glossary__pb2.TermNameRequest.SerializeToString,
                response_deserializer=app_dot_glossary__pb2.Term.FromString,
                _registered_method=True)
        self.UpdateTerm = channel.unary_unary(
                '/dictionary.GlossaryService/UpdateTerm',
                request_serializer=app_dot_glossary__pb2.Term.SerializeToString,
                response_deserializer=app_dot_glossary__pb2.MessageResponse.FromString,
                _registered_method=True)
        self.DeleteTerm = channel.unary_unary(
                '/dictionary.GlossaryService/DeleteTerm',
                request_serializer=app_dot_glossary__pb2.TermNameRequest.SerializeToString,
                response_deserializer=app_dot_glossary__pb2.MessageResponse.FromString,
                _registered_method=True)


class GlossaryServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetAllTerms(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddTerm(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTerm(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateTerm(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteTerm(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GlossaryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAllTerms': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllTerms,
                    request_deserializer=app_dot_glossary__pb2.Empty.FromString,
                    response_serializer=app_dot_glossary__pb2.TermsList.SerializeToString,
            ),
            'AddTerm': grpc.unary_unary_rpc_method_handler(
                    servicer.AddTerm,
                    request_deserializer=app_dot_glossary__pb2.Term.FromString,
                    response_serializer=app_dot_glossary__pb2.MessageResponse.SerializeToString,
            ),
            'GetTerm': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTerm,
                    request_deserializer=app_dot_glossary__pb2.TermNameRequest.FromString,
                    response_serializer=app_dot_glossary__pb2.Term.SerializeToString,
            ),
            'UpdateTerm': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateTerm,
                    request_deserializer=app_dot_glossary__pb2.Term.FromString,
                    response_serializer=app_dot_glossary__pb2.MessageResponse.SerializeToString,
            ),
            'DeleteTerm': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteTerm,
                    request_deserializer=app_dot_glossary__pb2.TermNameRequest.FromString,
                    response_serializer=app_dot_glossary__pb2.MessageResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'dictionary.GlossaryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('dictionary.GlossaryService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class GlossaryService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetAllTerms(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/dictionary.GlossaryService/GetAllTerms',
            app_dot_glossary__pb2.Empty.SerializeToString,
            app_dot_glossary__pb2.TermsList.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def AddTerm(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/dictionary.GlossaryService/AddTerm',
            app_dot_glossary__pb2.Term.SerializeToString,
            app_dot_glossary__pb2.MessageResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetTerm(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/dictionary.GlossaryService/GetTerm',
            app_dot_glossary__pb2.TermNameRequest.SerializeToString,
            app_dot_glossary__pb2.Term.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateTerm(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/dictionary.GlossaryService/UpdateTerm',
            app_dot_glossary__pb2.Term.SerializeToString,
            app_dot_glossary__pb2.MessageResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteTerm(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/dictionary.GlossaryService/DeleteTerm',
            app_dot_glossary__pb2.TermNameRequest.SerializeToString,
            app_dot_glossary__pb2.MessageResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)