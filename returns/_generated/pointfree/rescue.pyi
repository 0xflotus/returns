from typing import Callable, TypeVar, overload

from returns.context import (
    RequiresContextFutureResult,
    RequiresContextIOResult,
    RequiresContextResult,
)
from returns.future import FutureResult
from returns.io import IOResult
from returns.result import Result

# Result:
_ValueType = TypeVar('_ValueType', contravariant=True)
_ErrorType = TypeVar('_ErrorType')
_NewErrorType = TypeVar('_NewErrorType')

# Context:
_EnvType = TypeVar('_EnvType', contravariant=True)


@overload
def _rescue(
    function: Callable[[_ErrorType], Result[_ValueType, _NewErrorType]],
) -> Callable[
    [Result[_ValueType, _ErrorType]],
    Result[_ValueType, _NewErrorType],
]:
    ...


@overload
def _rescue(
    function: Callable[[_ErrorType], IOResult[_ValueType, _NewErrorType]],
) -> Callable[
    [IOResult[_ValueType, _ErrorType]],
    IOResult[_ValueType, _NewErrorType],
]:
    ...


@overload
def _rescue(
    function: Callable[
        [_ErrorType],
        RequiresContextResult[_EnvType, _ValueType, _NewErrorType],
    ],
) -> Callable[
    [RequiresContextResult[_EnvType, _ValueType, _ErrorType]],
    RequiresContextResult[_EnvType, _ValueType, _NewErrorType],
]:
    ...


@overload
def _rescue(
    function: Callable[
        [_ErrorType],
        RequiresContextIOResult[_EnvType, _ValueType, _NewErrorType],
    ],
) -> Callable[
    [RequiresContextIOResult[_EnvType, _ValueType, _ErrorType]],
    RequiresContextIOResult[_EnvType, _ValueType, _NewErrorType],
]:
    ...


@overload
def _rescue(
    function: Callable[
        [_ErrorType],
        RequiresContextFutureResult[_EnvType, _ValueType, _NewErrorType],
    ],
) -> Callable[
    [RequiresContextFutureResult[_EnvType, _ValueType, _ErrorType]],
    RequiresContextFutureResult[_EnvType, _ValueType, _NewErrorType],
]:
    ...


@overload
def _rescue(
    function: Callable[[_ErrorType], FutureResult[_ValueType, _NewErrorType]],
) -> Callable[
    [FutureResult[_ValueType, _ErrorType]],
    FutureResult[_ValueType, _NewErrorType],
]:
    ...
