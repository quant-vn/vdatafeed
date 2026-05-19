""" Models for SSI datafeed. """
from typing import Optional
from ...utils import BaseModel, Field, AliasChoices, model_validator


class SecuritiesInfo(BaseModel):
    """Securities information model."""
    instrument: Optional[str] = Field(validation_alias=AliasChoices('instrument', 'Symbol'))
    instrument_name: Optional[str] = Field(
        validation_alias=AliasChoices('instrument_name', 'SymbolName')
    )
    securities_type: Optional[str] = Field(
        validation_alias=AliasChoices('securities_type', 'SecType')
    )
    exchange: Optional[str] = Field(validation_alias=AliasChoices('exchange', 'Exchange'))
    issuer: Optional[str] = Field(validation_alias=AliasChoices('issuer', 'Issuer'))
    lot_size: Optional[int] = Field(validation_alias=AliasChoices('lot_size', 'LotSize'))
    maturity_date: Optional[str] = Field(
        validation_alias=AliasChoices('maturity_date', 'MaturityDate')
    )
    last_trading_date: Optional[str] = Field(
        validation_alias=AliasChoices('last_trading_date', 'LastTradingDate')
    )
    contract_multiplier: Optional[float] = Field(
        validation_alias=AliasChoices('contract_multiplier', 'ContractMultiplier')
    )
    underlying: Optional[str] = Field(validation_alias=AliasChoices('underlying', 'Underlying'))
    put_or_call: Optional[str] = Field(validation_alias=AliasChoices('put_or_call', 'PutOrCall'))
    exercise_price: Optional[float] = Field(
        validation_alias=AliasChoices('exercise_price', 'ExercisePrice')
    )
    exercise_style: Optional[str] = Field(
        validation_alias=AliasChoices('exercise_style', 'ExerciseStyle')
    )
    exercise_ratio: Optional[str] = Field(
        validation_alias=AliasChoices('exercise_ratio', 'ExcerciseRatio')
    )
    listed_share: Optional[float] = Field(
        validation_alias=AliasChoices('listed_share', 'ListedShare')
    )
    tick_price_1: Optional[float] = Field(validation_alias=AliasChoices('tick_price_1', 'TickPrice1'))
    tick_increment_1: Optional[float] = Field(
        validation_alias=AliasChoices('tick_increment_1', 'TickIncrement1')
    )
    tick_price_2: Optional[float] = Field(validation_alias=AliasChoices('tick_price_2', 'TickPrice2'))
    tick_increment_2: Optional[float] = Field(
        validation_alias=AliasChoices('tick_increment_2', 'TickIncrement2')
    )
    tick_price_3: Optional[float] = Field(validation_alias=AliasChoices('tick_price_3', 'TickPrice3'))
    tick_increment_3: Optional[float] = Field(
        validation_alias=AliasChoices('tick_increment_3', 'TickIncrement3')
    )


class IndexInfo(BaseModel):
    """Index information model."""
    index_code: Optional[str] = Field(validation_alias=AliasChoices('index_code', 'IndexCode'))
    exchange: Optional[str] = Field(validation_alias=AliasChoices('exchange', 'Exchange'))


class InstrumentInfo(BaseModel):
    """Daily instrument information model."""
    instrument: Optional[str] = Field(validation_alias=AliasChoices('instrument', 'Symbol'))
    trading_date: Optional[str] = Field(
        validation_alias=AliasChoices('trading_date', 'TradingDate')
    )
    price_change: Optional[float] = Field(
        validation_alias=AliasChoices('price_change', 'PriceChange')
    )
    per_price_change: Optional[float] = Field(
        validation_alias=AliasChoices('per_price_change', 'PerPriceChange')
    )
    ceiling: Optional[float] = Field(validation_alias=AliasChoices('ceiling', 'CeilingPrice'))
    floor: Optional[float] = Field(validation_alias=AliasChoices('floor', 'FloorPrice'))
    ref: Optional[float] = Field(validation_alias=AliasChoices('ref', 'RefPrice'))
    open: Optional[float] = Field(validation_alias=AliasChoices('open', 'OpenPrice'))
    high: Optional[float] = Field(validation_alias=AliasChoices('high', 'HighestPrice'))
    low: Optional[float] = Field(validation_alias=AliasChoices('low', 'LowestPrice'))
    close: Optional[float] = Field(validation_alias=AliasChoices('close', 'ClosePrice'))
    avg_price: Optional[float] = Field(validation_alias=AliasChoices('avg_price', 'AveragePrice'))
    close_adj: Optional[float] = Field(
        validation_alias=AliasChoices('close_adj', 'ClosePriceAdjusted')
    )
    total_vol: Optional[float] = Field(validation_alias=AliasChoices('total_vol', 'TotalMatchVol'))
    total_val: Optional[float] = Field(validation_alias=AliasChoices('total_val', 'TotalMatchVal'))
    total_deal_val: Optional[float] = Field(
        validation_alias=AliasChoices('total_deal_val', 'TotalDealVal')
    )
    total_deal_vol: Optional[float] = Field(
        validation_alias=AliasChoices('total_deal_vol', 'TotalDealVol')
    )
    foreign_current_room: Optional[float] = Field(
        validation_alias=AliasChoices('foreign_current_room', 'ForeignCurrentRoom')
    )
    total_foreign_buy_vol: Optional[float] = Field(
        validation_alias=AliasChoices('total_foreign_buy_vol', 'ForeignBuyVolTotal')
    )
    total_foreign_buy_val: Optional[float] = Field(
        validation_alias=AliasChoices('total_foreign_buy_val', 'ForeignBuyValTotal')
    )
    total_foreign_sell_val: Optional[float] = Field(
        validation_alias=AliasChoices('total_foreign_sell_val', 'ForeignSellValTotal')
    )
    total_foreign_sell_vol: Optional[float] = Field(
        validation_alias=AliasChoices('total_foreign_sell_vol', 'ForeignSellVolTotal')
    )
    total_buy_trade: Optional[int] = Field(
        validation_alias=AliasChoices('total_buy_trade', 'TotalBuyTrade')
    )
    total_buy_trade_vol: Optional[float] = Field(
        validation_alias=AliasChoices('total_buy_trade_vol', 'TotalBuyTradeVol')
    )
    total_sell_trade: Optional[int] = Field(
        validation_alias=AliasChoices('total_sell_trade', 'TotalSellTrade')
    )
    total_sell_trade_vol: Optional[float] = Field(
        validation_alias=AliasChoices('total_sell_trade_vol', 'TotalSellTradeVol')
    )
    net_buy_sell_vol: Optional[float] = Field(
        validation_alias=AliasChoices('net_buy_sell_vol', 'NetBuySellVol')
    )
    net_buy_sell_val: Optional[float] = Field(
        validation_alias=AliasChoices('net_buy_sell_val', 'NetBuySellVal')
    )
    total_trade_vol: Optional[float] = Field(
        validation_alias=AliasChoices('total_trade_vol', 'TotalTradedVol')
    )
    total_trade_val: Optional[float] = Field(
        validation_alias=AliasChoices('total_trade_val', 'TotalTradedValue')
    )


class IndicesInfo(BaseModel):
    """Indices information model."""
    index_code: Optional[str] = Field(validation_alias=AliasChoices('index', 'IndexId'))
    trading_date: Optional[str] = Field(
        validation_alias=AliasChoices('trading_date', 'TradingDate')
    )
    name: Optional[str] = Field(validation_alias=AliasChoices('name', 'IndexName'))
    session: Optional[str] = Field(validation_alias=AliasChoices('session', 'TradingSession'))
    value: Optional[float] = Field(validation_alias=AliasChoices('value', 'IndexValue'))
    change: Optional[float] = Field(validation_alias=AliasChoices('change', 'Change'))
    change_percent: Optional[float] = Field(
        validation_alias=AliasChoices('change_percent', 'RatioChange')
    )
    total_trade: Optional[int] = Field(validation_alias=AliasChoices('total_trade', 'TotalTrade'))
    total_match_vol: Optional[float] = Field(
        validation_alias=AliasChoices('total_match_vol', 'TotalMatchVol')
    )
    total_match_val: Optional[float] = Field(
        validation_alias=AliasChoices('total_match_val', 'TotalMatchVal')
    )
    up_count: Optional[int] = Field(validation_alias=AliasChoices('advances', 'Advances'))
    no_change_count: Optional[int] = Field(validation_alias=AliasChoices('no_changes', 'NoChanges'))
    down_count: Optional[int] = Field(validation_alias=AliasChoices('declines', 'Declines'))
    ceiling_count: Optional[int] = Field(validation_alias=AliasChoices('ceiling', 'Ceilings'))
    floor_count: Optional[int] = Field(validation_alias=AliasChoices('floor', 'Floors'))
    total_deal_vol: Optional[float] = Field(
        validation_alias=AliasChoices('total_deal_vol', 'TotalDealVol')
    )
    total_deal_val: Optional[float] = Field(
        validation_alias=AliasChoices('total_deal_val', 'TotalDealVal')
    )
    total_vol: Optional[float] = Field(validation_alias=AliasChoices('total_vol', 'TotalVol'))
    total_val: Optional[float] = Field(validation_alias=AliasChoices('total_val', 'TotalVal'))


class EndOfDayOHLC(BaseModel):
    """End-of-day OHLC data model."""
    instrument: Optional[str] = Field(validation_alias=AliasChoices('instrument', 'Symbol'))
    exchange: Optional[str] = Field(validation_alias=AliasChoices('exchange', 'Market'))
    trading_date: Optional[str] = Field(
        validation_alias=AliasChoices('trading_date', 'TradingDate')
    )
    open: Optional[float] = Field(validation_alias=AliasChoices('open', 'Open'))
    high: Optional[float] = Field(validation_alias=AliasChoices('high', 'High'))
    low: Optional[float] = Field(validation_alias=AliasChoices('low', 'Low'))
    close: Optional[float] = Field(validation_alias=AliasChoices('close', 'Close'))
    vol: Optional[float] = Field(validation_alias=AliasChoices('vol', 'Volume'))
    val: Optional[float] = Field(validation_alias=AliasChoices('val', 'Value'))


class IntradayOHLC(BaseModel):
    """Intraday OHLC data model."""
    instrument: Optional[str] = Field(validation_alias=AliasChoices('instrument', 'Symbol'))
    trading_date: Optional[str] = Field(
        validation_alias=AliasChoices('trading_date', 'TradingDate')
    )
    trading_time: Optional[str] = Field(validation_alias=AliasChoices('trading_time', 'Time'))
    open: Optional[float] = Field(validation_alias=AliasChoices('open', 'Open'))
    high: Optional[float] = Field(validation_alias=AliasChoices('high', 'High'))
    low: Optional[float] = Field(validation_alias=AliasChoices('low', 'Low'))
    close: Optional[float] = Field(validation_alias=AliasChoices('close', 'Close'))
    vol: Optional[float] = Field(validation_alias=AliasChoices('vol', 'Volume'))
    val: Optional[float] = Field(validation_alias=AliasChoices('val', 'Value'))


class TradeTick(BaseModel):
    """Real-time trade tick model."""
    datetime: Optional[str] = None
    symbol: Optional[str] = Field(validation_alias=AliasChoices('symbol', 'Symbol'))
    ceiling: Optional[float] = Field(validation_alias=AliasChoices('ceiling', 'Ceiling'))
    floor: Optional[float] = Field(validation_alias=AliasChoices('floor', 'Floor'))
    ref_price: Optional[float] = Field(validation_alias=AliasChoices('ref_price', 'RefPrice'))
    price: Optional[float] = Field(validation_alias=AliasChoices('price', 'LastPrice'))
    vol: Optional[float] = Field(validation_alias=AliasChoices('vol', 'LastVol'))
    total_vol: Optional[float] = Field(validation_alias=AliasChoices('total_vol', 'TotalVol'))
    total_val: Optional[float] = Field(validation_alias=AliasChoices('total_val', 'TotalVal'))

    @model_validator(mode='before')
    def set_custom_field(cls, values):
        values['datetime'] = ' '.join([
            "-".join(reversed(values.get('TradingDate').split("/"))),
            values.get('Time')
        ])
        return values


class QuoteTick(BaseModel):
    """Real-time quote tick model."""
    datetime: Optional[str] = None
    symbol: Optional[str] = Field(validation_alias=AliasChoices('symbol', 'Symbol'))
    ceiling: Optional[float] = Field(validation_alias=AliasChoices('ceiling', 'Ceiling'))
    floor: Optional[float] = Field(validation_alias=AliasChoices('floor', 'Floor'))
    ref_price: Optional[float] = Field(validation_alias=AliasChoices('ref_price', 'RefPrice'))
    bid_price: Optional[list] = []
    bid_vol: Optional[list] = []
    ask_price: Optional[list] = []
    ask_vol: Optional[list] = []

    @model_validator(mode='before')
    def set_custom_field(cls, values):
        values['datetime'] = ' '.join([
            "-".join(reversed(values.get('TradingDate').split("/"))),
            values.get('Time')
        ])
        _l = range(1, 11)
        _rev_l = list(reversed(_l))
        values['bid_price'] = [values.get(f"BidPrice{i}") for i in _rev_l]
        values['bid_vol'] = [values.get(f"BidVol{i}") for i in _rev_l]
        values['ask_price'] = [values.get(f"AskPrice{i}") for i in _l]
        values['ask_vol'] = [values.get(f"AskVol{i}") for i in _l]
        return values


class IndexComponentInfo(BaseModel):
    """Index component information model."""
    index_code: Optional[str] = Field(validation_alias=AliasChoices('index_code', 'IndexCode'))
    index_name: Optional[str] = Field(validation_alias=AliasChoices('index_name', 'IndexName'))
    exchange: Optional[str] = Field(validation_alias=AliasChoices('exchange', 'Exchange'))
    instruments: Optional[list] = []

    @model_validator(mode='before')
    def set_instruments(cls, values):
        index_comp = values.get('IndexComponent', [])
        if index_comp:
            values['instruments'] = [item.get('StockSymbol') or item.get('Isin') for item in index_comp]
        return values
