# Supported Boards

Development board source code root directory: `customer/boards`

The source code path for each board is shown in the **Board Directory** column in the table. For example, the code for development board 551-HDK is in the `eh-lb551` directory. This directory name is also used as the board name when compiling.

For boards with multi-core chips, each board directory contains subdirectories organized by core. As shown in the figure below, the eh-lb551 directory has two subdirectories: `hcpu` and `lcpu`, which store the configuration code for the HCPU and LCPU of the SF32LB551 chip respectively. When using `scons --board=<board_name>` to compile a program for a specific board, if no core is specified, the HCPU configuration is used by default. To specify the LCPU configuration, add the `_lcpu` suffix. For example, both `scons --board=eh-lb551` and `scons --board=eh-lb551_hcpu` compile with the 551-HDK's HCPU configuration, and the generated image files are saved in the `build_eh-lb551_hcpu` directory, while `scons --board=eh-lb551_lcpu` compiles with the 551-HDK's LCPU configuration, and the generated image files are saved in the `build_eh-lb551_lcpu` directory.

For currently available development boards, we have created a naming convention, generally following the pattern `model-type_memory-type_display-interface`. Note that memory type and display interface may be omitted.

Memory type naming rules:

- A: Indicates the board uses SPI NAND memory, followed by the memory capacity in MB
- N: Indicates the board uses SPI NOR memory, followed by the memory capacity in MB
- R: Indicates the board uses SPI PSRAM memory, followed by the memory capacity in MB
- E: Indicates the board uses eMMC memory, followed by the memory capacity in GB

For example, `a128r32n1` indicates 128MB SPI NAND memory, 32MB SPI PSRAM memory, and 1MB SPI NOR memory.

Some typical examples:

- `sf32lb52-nano_n4`: Indicates the Nano version development board of model SF32LB52, using 4MB SPI NOR memory.
- `sf32lb56-lcd_a128r12n1`: Indicates the LCD version development board of model SF32LB56, using 128MB SPI NAND memory, 12MB SPI PSRAM memory, and 1MB SPI NOR memory.

```{image} ../../assets/folder.png
:scale: 70%
```

<!-- 
| left | center | right |
| :--- | :----: | ----: |
| a    | b      | c     | -->


## SF32LB55x Series

Name         |  Model        |    Board Directory   |    
-------------|---------------|----------------------|
551-HDK      | EH-SS6600A8   |   eh-lb551          | 
555-HDK      | EH-SF32LB555  |   eh-lb555          | 


The boards in the following table are no longer maintained and cannot be used for project compilation, but the directories are still retained
Name         |  Model        |    Board Directory      |    
-------------|---------------|-------------------------|
551-EVB      | EC-LB551      |   ec-lb551xxx          | 
555-EVB      | EC-LB555      |   ec-lb555xxx          | 
557-EVB      | EC-LB557      |   ec-lb557xxx          | 
6600-HDK     | EH-SS6600     |   eh-ss6600xxx         | 


## SF32LB58x Series

Abbreviation |  Model                    |    Board Directory   |    
-------------|---------------------------|----------------------|
583-EVB      | SF32LB58X_EVB_CORE(583)   |   ec-lb583          | 
585-EVB      | SF32LB58X_EVB_CORE(585)   |   ec-lb585          | 
587-EVB       | SF32LB58X_EVB_CORE(587)   |   [ec-lb587](boards/ec-lb587/doc/index.md)    | 
58-LCD_A128R32N1_DSI | SF32LB58-DevKit-LCD_A128R32N1_DSI |   [sf32lb58-lcd_a128r32n1_dsi](boards/sf32lb58-lcd_a128r32n1_dsi/doc/index.md)    |
58-LCD_N16R32N1_DPI | SF32LB58-DevKit-LCD_LCD_N16R32N1_DPI |   [sf32lb58-lcd_n16r32n1_dpi](boards/sf32lb58-lcd_n16r32n1_dpi/doc/index.md)    |
58-LCD_N16R32N1_DSI | SF32LB58-DevKit-LCD_N16R32N1_DSI |   [sf32lb58-lcd_n16r32n1_dsi](boards/sf32lb58-lcd_n16r32n1_dsi/doc/index.md)    |
58-LCD_N16R64N4 | SF32LB58-DevKit-LCD_N16R64N4 |   [sf32lb58-lcd-n16r64n4](boards/sf32lb58-lcd_n16r64n4/doc/index.md)    |

## SF32LB56x Series

Abbreviation  |  Model                    |    Board Directory   |    
--------------|---------------------------|----------------------|
567-EVB       | EC-LB56XV(567)            |   ec-lb567          | 
561-HDK       | EH-SF32LB56XU(561)        |   eh-lb561          | 
563-HDK       | EH-SF32LB56XU(561)        |   eh-lb563          | 
6700-HDK      | EH-SF32LB56XU(6700)       |   eh-ss6700         | 
56-LCD_A128R12N1 | SF32LB56-DevKit-LCD_A128R12N1 |   [sf32lb56-lcd_a128r12n1](boards/sf32lb56-lcd_a128r12n1/doc/index.md)    |
56-LCD_N16R12N1 | SF32LB56-DevKit-LCD_N16R12N1 |   [sf32lb56-lcd_n16r12n1](boards/sf32lb56-lcd_n16r12n1/doc/index.md)    |


The boards in the following table are no longer maintained and cannot be used for project compilation, but the directories are still retained

Name         |  Model        |    Board Directory      |    
-------------|---------------|-------------------------|
561-EVB      | EC-LB561      |   ec-lb561xxx          | 
563-EVB      | EC-LB563      |   ec-lb563xxx          | 



## SF32LB52x Series

Abbreviation |  Model                    |    Board Directory   |    
-------------|---------------------------|----------------------|
520-HDK      | EH-SF32LB52X(520)         |   eh-lb520          | 
523-HDK      | EH-SF32LB52X(523)         |   eh-lb523          | 
525-HDK      | EH-SF32LB52X(525)         |   eh-lb525          | 
6500-HDK     | EH-SF32LB52X(6500)        |   eh-lb6500         | 
NANO-N4      | SF32LB52-NANO_N4          |   sf32lb52-nano_n4 | 
NANO-N16R16  | SF32LB52-NANO_N16R16      |   sf32lb52-nano_n16r16 | 
��ɽ��(LCHSPI-ULP)     | SF32LB52-LCHSPI-ULP         |   sf32lb52-lchspi-ulp    |
52-LCD_N16R8 | SF32LB52-DevKit-LCD_N16R8 |   [sf32lb52-lcd_n16r8](boards/sf32lb52-lcd_n16r8/doc/index.md)    |
52-LCD_52D | SF32LB52-DevKit-LCD_52D |   [sf32lb52-lcd_52d](boards/sf32lb52-lcd_52d/doc/index.md)    |


```{toctree}
:titlesonly:
:glob:

boards/ec-lb587/doc/index
boards/ec-lb587_a2/doc/index
boards/sf32lb52-core_e8r16/doc/index
boards/sf32lb52-core_n16r16/doc/index
boards/sf32lb52-lcd_52d/doc/index
boards/sf32lb52-lcd_n16r8/doc/index.
boards/sf32lb52-lcd_n16r8_jdi/doc/index
boards/sf32lb56-lcd_a128r12n1/doc/index
boards/sf32lb56-lcd_n16r12n1/doc/index
boards/sf32lb58-lcd_a128r32n1_dsi/doc/index
boards/sf32lb58-lcd_n16r32n1_dpi/doc/index
boards/sf32lb58-lcd_n16r32n1_dsi/doc/index
boards/sf32lb58-lcd_n16r64n4/doc/index

```