from __future__ import annotations

from typing import Any, Dict, List

from pydantic import BaseModel, Field


class Metrics(BaseModel):
    MeshMetric___MeshStoreBackups_count: int = Field(
        ..., alias='MeshMetric - MeshStoreBackups count'
    )
    MeshMetric___MeshFlows_count: int = Field(..., alias='MeshMetric - MeshFlows count')
    MeshMetric___MeshStores_count: int = Field(
        ..., alias='MeshMetric - MeshStores count'
    )
    MeshMetric___Methods_count: int = Field(..., alias='MeshMetric - Methods count')
    MeshMetric___MeshBotTypes_count: int = Field(
        ..., alias='MeshMetric - MeshBotTypes count'
    )
    MeshMetric___MeshBotInstances_count: int = Field(
        ..., alias='MeshMetric - MeshBotInstances count'
    )


class Mesh(BaseModel):
    name: str
    integrity_store: str
    created_by: str
    created_at: str
    metrics: Metrics


class MeshBot(BaseModel):
    MeshBotInstance_Name: str = Field(..., alias='MeshBotInstance Name')
    MeshBotInstance_Seq: int = Field(..., alias='MeshBotInstance Seq')


class Specs(BaseModel):
    MeshFlow_id: int
    MeshBots: List[MeshBot]


class Metrics1(BaseModel):
    MeshFlow_id: int
    MeshFlowMetric___MeshBotInstance_count: int = Field(
        ..., alias='MeshFlowMetric - MeshBotInstance count'
    )


class Metadata(BaseModel):
    MeshFlow_id: int
    Created_By: str = Field(..., alias='Created By')


class MeshFlow(BaseModel):
    MeshFlow_id: int
    MeshFlow_name: str
    Specs: Specs
    Metrics: Metrics1
    Metadata: Metadata


class StateMethod(BaseModel):
    Method: str
    Method_Seq: int = Field(..., alias='Method Seq')
    Method_Specs_URL: str = Field(..., alias='Method Specs URL')
    Schedule: str


class State(BaseModel):
    State: str
    State_Seq: int = Field(..., alias='State Seq')
    state_methods: List[StateMethod]


class Specs1(BaseModel):
    MeshBotInstance_id: int
    states: List[State]


class Metadata1(BaseModel):
    MeshBotInstance_id: int
    Created_By: str = Field(..., alias='Created By')


class MeshBotInstanceItem(BaseModel):
    MeshBotInstance_name: str
    MeshBotInstance_id: int
    MeshBotType_nm: str
    Specs: Specs1
    Metrics: Dict[str, Any]
    Metadata: Metadata1


class StateMethod1(BaseModel):
    Method: str
    Method_Seq: int = Field(..., alias='Method Seq')


class State1(BaseModel):
    State: str
    State_Seq: int = Field(..., alias='State Seq')
    state_methods: List[StateMethod1]


class Specs2(BaseModel):
    MeshBotType_id: int
    states: List[State1]


class Metrics2(BaseModel):
    MeshBotType_id: int
    MeshBotTypeMetric___MeshBotInstance_Count: int = Field(
        ..., alias='MeshBotTypeMetric - MeshBotInstance Count'
    )
    MeshBotTypeMetric___Method_Count: int = Field(
        ..., alias='MeshBotTypeMetric - Method Count'
    )


class Metadata2(BaseModel):
    MeshBotType_id: int
    Created_By: str = Field(..., alias='Created By')


class MeshBotType(BaseModel):
    MeshBotType_name: str
    MeshBotType_id: int
    Specs: Specs2
    Metrics: Metrics2
    Metadata: Metadata2


class Specs3(BaseModel):
    MeshStore_id: int
    Is_Secure: int = Field(..., alias='Is Secure')
    Store_Data_Type: str = Field(..., alias='Store Data Type')
    Store_Key: str = Field(..., alias='Store Key')
    Can_Write: int = Field(..., alias='Can Write')
    Can_Read: int = Field(..., alias='Can Read')


class Metrics3(BaseModel):
    MeshStore_id: int
    Successors: int
    User_Tags: int = Field(..., alias='User Tags')
    Variable: int
    Doctor: int
    Patient: int
    Access_Tags: int = Field(..., alias='Access Tags')
    Date_Updated: int = Field(..., alias='Date Updated')
    Lineage: int
    Status_Tags: int = Field(..., alias='Status Tags')
    Security_Tags: int = Field(..., alias='Security Tags')


class Metadata3(BaseModel):
    MeshStore_id: int
    Created_By: str = Field(..., alias='Created By')


class Store(BaseModel):
    MeshStore_name: str
    MeshStore_id: int
    Specs: Specs3
    Metrics: Metrics3
    Metadata: Metadata3


class GetResponseSchema(BaseModel):
    Mesh: Mesh
    MeshFlows: List[MeshFlow]
    MeshBotInstance: List[MeshBotInstanceItem]
    MeshBotTypes: List[MeshBotType]
    Stores: List[Store]
