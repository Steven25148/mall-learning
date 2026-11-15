package com.macro.mall.dto;

import io.swagger.v3.oas.annotations.media.Schema;
import lombok.Getter;
import lombok.Setter;

/**
 * 订单查询参数
 * Created by macro on 2018/10/11.
 */
@Getter
@Setter
public class OmsOrderQueryParam {
    @Schema(title =  "订单编号", example = "201809150101000001")
    private String orderSn;
    @Schema(title =  "收货人姓名/号码", example = "大梨")
    private String receiverKeyword;
    @Schema(title =  "订单状态：0->待付款；1->待发货；2->已发货；3->已完成；4->已关闭；5->无效订单",
            example = "4", allowableValues = {"0", "1", "2", "3", "4", "5"})
    private Integer status;
    @Schema(title =  "订单类型：0->正常订单；1->秒杀订单",
            example = "0", allowableValues = {"0", "1"})
    private Integer orderType;
    @Schema(title =  "订单来源：0->PC订单；1->app订单",
            example = "1", allowableValues = {"0", "1"})
    private Integer sourceType;
    @Schema(title =  "订单提交日期，格式：yyyy-MM-dd", example = "2018-09-15")
    private String createTime;
}
