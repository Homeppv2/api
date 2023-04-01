from homepp.core.common.uow import UnitOfWork


class FakeUnitOfWork(UnitOfWork):
    async def commit(self) -> None:
        pass

    async def rollback(self) -> None:
        pass
